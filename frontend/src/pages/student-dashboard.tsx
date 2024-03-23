import Row from "../components/student-dashboard/row";

function StudentDashboard() {
  return (
    <div className="flex h-screen items-center justify-center bg-gradient-to-bl from-gray-600 via-gray-700 to-gray-800 text-white">
      <div className="mx-auto w-[90vw] max-w-7xl">
        <p className="text-4xl font-bold">Your Classrooms</p>
        <Row title="Lmao" />
      </div>
    </div>
  );
}

export default StudentDashboard;
