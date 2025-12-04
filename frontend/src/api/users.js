import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export const createUser = async (user) => {
  try {
    const res = await axios.post(`${API_URL}/users_db`, user);
    return res.data;
  } catch (err) {
    console.error(err);
    throw err;
  }
};
