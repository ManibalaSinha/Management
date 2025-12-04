// frontend/src/api/auth.js
import axios from "axios";

export const loginUser = async (username, password) => {
  try {
    const res = await axios.post("http://127.0.0.1:8000/auth/login", {
      username,
      password,
    });
    return res.data;
  } catch (err) {
    console.error(err);
    throw err;
  }
};
