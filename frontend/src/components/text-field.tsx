import { ChangeEvent } from "react";

type TextFieldType = "text" | "number" | "password";

interface ITextField {
  title: string;
  htmlId: string;

  defaultValue?: string;
  required?: boolean;

  type?: TextFieldType;
  placeholder?: string;

  numberMin?: number;
  numberMax?: number;

  onChange?(event: ChangeEvent<HTMLInputElement>): void;
}

export default function TextField(props: ITextField) {
  if (props.type === null) {
    props.type = "text";
  }

  return (
    <div className="block text-left">
      <label
        htmlFor={props.htmlId}
        className="mb-1 block text-sm font-medium text-gray-900"
      >
        <p className="text-gray-900">
          <span>{props.title}</span>{" "}
          <span className="text-sm font-light">
            {props.required ? "" : " (optional)"}
          </span>
        </p>
      </label>
      <input
        type={props.type}
        id={props.htmlId}
        className="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-red-500 focus:ring-red-500"
        placeholder={props.placeholder}
        min={props.numberMin}
        max={props.numberMax}
        defaultValue={props.defaultValue}
        required={props.required}
        onChange={props.onChange}
      />
    </div>
  );
}
