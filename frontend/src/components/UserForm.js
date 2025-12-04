import React, { useState } from "react";
import { createUser } from "../api/users";

function UserForm() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault(); // Prevent form reload
    try {
      const data = await createUser({ name, email });
      console.log(data);
      alert("User added successfully!");
      setName("");  // Clear form
      setEmail("");
    } catch (err) {
      console.error(err);
      alert("Error adding user");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        placeholder="Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
        required
      />
      <input
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        type="email"
        required
      />
      <button type="submit">Add User</button>
    </form>
  );
}

export default UserForm;
