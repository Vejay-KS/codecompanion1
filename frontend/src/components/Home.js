import React from "react";
import '../App.css';
import CodeOptimizerFormUI from "./CodeOptimizer";
import CodeDebuggerFormUI from "./CodeDebugger";
import CodeReviewerFormUI from "./CodeReviewer";
import CommentGeneratorFormUI from "./CommentGenerator";

const HomePage = () => {
  const [activeSection, setActiveSection] = React.useState("code-optimiser");

  const handleSectionChange = (sectionName) => {
    setActiveSection(sectionName);
  };

  const renderSection = () => {
    switch (activeSection) {
      case "code-optimiser":
        return <CodeOptimizerFormUI/>;
      case "code-debugger":
        return <CodeDebuggerFormUI/>;
      case "code-reviewer":
        return <CodeReviewerFormUI/>;
      case "comment-generator":
        return <CommentGeneratorFormUI/>;
      default:
        return <div>No section selected</div>;
    }
  };

  return (
    <div className="App">
      <nav>
        <div className="logo">#CodeCompanion</div>
        <button onClick={() => handleSectionChange("code-optimiser")}>
          Code Optimiser
        </button>
        <button onClick={() => handleSectionChange("code-debugger")}>
          Code Debugger
        </button>
        <button onClick={() => handleSectionChange("code-reviewer")}>
          Code Reviewer
        </button>
        <button onClick={() => handleSectionChange("comment-generator")}>
          Comment Generator
        </button>


        {/* This section needs to be editied for logout  */}
        <button onClick={() => handleSectionChange("comment-generator")}> 
          Log Out
        </button>


      </nav>
      <main>{renderSection()}</main>
      {/* <div className="text-input-container">
        <textarea placeholder="Type your code here..."></textarea>
        <button>Submit</button>
      </div> */}
    </div>
  );
};

const CodeOptimiser = () => {
  return <div className="header">Code Optimiser</div>;
};

const CodeDebugger = () => {
  return <div className="header">Code Debugger</div>;
};

const CodeReviewer = () => {
  return <div className="header">Code Reviewer</div>;
};

const CommentGenerator = () => {
  return <div className="header">Comment Generator</div>;
};

export default HomePage;