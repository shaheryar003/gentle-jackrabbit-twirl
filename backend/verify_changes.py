import subprocess
import time
import sys
import os
import signal
import threading

def read_stream(stream, prefix):
    for line in iter(stream.readline, ''):
        print(f"[{prefix}] {line.strip()}")
    stream.close()

def verify_changes():
    # 1. Start the backend server on port 8002
    print("Starting backend server on port 8002...")
    process = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "backend.main:app", "--host", "127.0.0.1", "--port", "8002"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=os.environ.copy(),
        text=True,
        bufsize=1
    )

    # Start threads to read server output
    stdout_thread = threading.Thread(target=read_stream, args=(process.stdout, "SERVER_OUT"))
    stderr_thread = threading.Thread(target=read_stream, args=(process.stderr, "SERVER_ERR"))
    stdout_thread.daemon = True
    stderr_thread.daemon = True
    stdout_thread.start()
    stderr_thread.start()

    # Wait for server to start
    print("Waiting for server to start...")
    time.sleep(5) 

    if process.poll() is not None:
        print("Server failed to start immediately.")
        sys.exit(1)

    try:
        # 2. Run the test script against port 8002
        print("Running auth flow test...")
        test_result = subprocess.run(
            [sys.executable, "backend/test_auth_flow.py", "8002"],
            capture_output=False,  # Stream output directly to console
            text=True
        )

        if test_result.returncode == 0:
            print("\nSUCCESS: Authentication flow verified successfully.")
        else:
            print("\nFAILURE: Authentication flow test failed.")
            sys.exit(1)

    finally:
        # 3. Shutdown the server
        print("Shutting down server...")
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()

if __name__ == "__main__":
    verify_changes()