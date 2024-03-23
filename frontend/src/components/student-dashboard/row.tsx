interface IRow {
  title: string;
}

function Row(props: IRow) {
  return <div className="rounded-lg">{props.title}</div>;
}

export default Row;
