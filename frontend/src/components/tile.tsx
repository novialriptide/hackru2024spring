interface ITile {
  children: JSX.Element;
}

export default function Tile(props: ITile) {
  return <div className="rounded-lg bg-gray-200 p-8">{props.children}</div>;
}
