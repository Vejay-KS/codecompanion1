// Register.js

import React from "react";
import '../App.css';  // Importing your styles

const Register = () => {
  return (
    <div className="register">
      <h2>Register</h2>
      <form>
        <input type="text" placeholder="Username" />
        <input type="email" placeholder="Email" />
        <input type="password" placeholder="Password" />
        <input type="password" placeholder="Confirm Password" />
        <select className="userdropdown">
            <option value="student">Developer</option>
            <option value="teacher">Developer Manager</option>
            <option value="principal">HR Manager</option>
        </select>
        <button type="submit">Register</button>
      </form>
    </div>
  );
};

export default Register;