// import React, { useState } from 'react';
// import axios from 'axios';
// import { API_URL } from '../constants';
// axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
// axios.defaults.xsrfCookieName = "xcsrftoken";

// const CodeDebuggerFormUI = () => {
//   const [inputCode, setInputCode] = useState('');
//   const [codeCompletion, setCodeCompletion] = useState('');

//   const handleSubmit = async (e) => {
//     console.log("check debug");
//     e.preventDefault();

//     try {
//       const response = await axios.post("http://127.0.0.1:8000/codeDebugger/", {
//         input_code: inputCode,
//       });
//       const { code_completion } = response.data;
//       setCodeCompletion(code_completion);
//     } catch (error) {
//       console.error(error);
//     }
//   };

//   return (
//     <div className="input-container">
//       <input type="text" value={inputCode} onChange={(e) => setInputCode(e.target.value)} />
//       <button onClick={handleSubmit}>Debug Code</button>
//       <div>{codeCompletion}</div>
//     </div>
//   );
// };

// export default CodeDebuggerFormUI;

import React, { useState } from "react";
import axios from "axios";

const CodeDebuggerFormUI = () => {
  const [inputCode, setInputCode] = useState("");
  const [inputFile, setInputFile] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("input_code", inputCode);
    formData.append("input_file", inputFile);

    axios.post("http://127.0.0.1:8000/codeDebugger/", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    })
      .then((response) => {
        // Handle success
        console.log(response.data);
      })
      .catch((error) => {
        // Handle error
        console.error(error);
      });
  };

  const handleInputCodeChange = (e) => {
    setInputCode(e.target.value);
  };

  const handleInputFileChange = (e) => {
    setInputFile(e.target.files[0]);
  };

  return (
    <div className="text-input-container">
    <form onSubmit={handleSubmit}>
      <textarea
        name="input_code"
        value={inputCode}
        onChange={handleInputCodeChange}
      />
      <input
        type="file"
        name="input_file"
        onChange={handleInputFileChange}
      />

      <button type="submit">Debug Code</button>
    </form>
    </div>
  );
};

export default CodeDebuggerFormUI;
