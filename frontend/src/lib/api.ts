import { MuseumTheme, MuseumObject } from "@/types";

const API_BASE_URL = "https://gentle-jackrabbit-twirl-backend.onrender.com/api/v1";

export async function fetchThemes(): Promise<MuseumTheme[]> {
  const response = await fetch(`${API_BASE_URL}/themes`);
  if (!response.ok) {
    throw new Error(`Failed to fetch themes: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTheme(id: string): Promise<MuseumTheme> {
  const response = await fetch(`${API_BASE_URL}/themes/${id}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch theme: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchObject(id: string): Promise<MuseumObject> {
  const response = await fetch(`${API_BASE_URL}/objects/${id}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch object: ${response.statusText}`);
  }
  return response.json();
}

export async function fetchTour(themeId: string, size: string): Promise<MuseumObject[]> {
  const response = await fetch(`${API_BASE_URL}/tours/${themeId}/${size}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch tour: ${response.statusText}`);
  }
  return response.json();
}

export async function signup(email: string, password: string): Promise<any> {
  const response = await fetch(`${API_BASE_URL}/auth/signup`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ email, password }),
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || `Failed to signup: ${response.statusText}`);
  }
  return response.json();
}