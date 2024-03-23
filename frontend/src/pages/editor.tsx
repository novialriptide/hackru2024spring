import React, { useEffect, useState } from "react";
import MonacoEditor, { MonacoEditorProps } from "react-monaco-editor";
import Markdown from "react-markdown";
import Button from "../components/button";

interface IEditor extends MonacoEditorProps {}

function Editor(props: IEditor) {
  const [editorHeight, setEditorHeight] = useState<number>(window.innerHeight);
  const [editorWidth, setEditorWidth] = useState<number>(window.innerWidth / 2);

  const instructions = "## Testing\n### Markdown\nIt **works**?";

  useEffect(() => {
    const handleResize = () => {
      setEditorHeight(window.innerHeight);
      setEditorWidth(window.innerWidth / 2);
    };

    window.addEventListener("resize", handleResize);

    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, []);

  function editorDidMount(editor: any, monaco: any) {
    console.log("editorDidMount", editor);
    // You can access the editor instance here if you need to do something with it
  }

  function onChange(newValue: string, e: any) {
    console.log("onChange", newValue, e);
  }

  return (
    <div className="flex h-screen">
      <MonacoEditor
        width={`${editorWidth}px`}
        height={`${editorHeight}px`}
        language="python"
        theme="vs-dark"
        defaultValue="# Start coding here!"
        editorDidMount={editorDidMount}
        onChange={onChange}
        {...props}
      />
      <div className="static">
        <Markdown className="prose lg:prose-xl">{instructions}</Markdown>
        <div className="absolute bottom-0 w-full px-4">
          <Button>
            <p>Submit</p>
          </Button>
        </div>
      </div>
    </div>
  );
}

export default Editor;
