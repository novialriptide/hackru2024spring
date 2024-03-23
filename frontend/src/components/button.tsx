interface IButton {
  children: JSX.Element;

  onClick?(): void;
}

export default function Button(props: IButton) {
  return (
    <button
      onClick={props.onClick}
      type="button"
      className="mb-2 me-2 rounded-lg border border-gray-300 bg-gray-50 px-5 py-2.5 text-sm font-medium hover:bg-gray-300 focus:outline-none focus:ring-4 focus:ring-gray-300"
    >
      {props.children}
    </button>
  );
}
