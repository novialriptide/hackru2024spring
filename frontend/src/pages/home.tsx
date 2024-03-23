import { useNavigate } from "react-router-dom";
import Button from "../components/button";

function Home() {
  const navigate = useNavigate();

  return (
    <div>
      <div className="flex h-screen items-center justify-center bg-gradient-to-bl from-gray-600 via-gray-700 to-gray-800 text-center">
        <div>
          <p className="text-6xl font-black text-white">Untitled Coding App</p>
          <p className="text-lg text-white">Learn with your peers</p>
          <div className="pt-2">
            <Button
              onClick={() => {
                navigate("/login");
              }}
            >
              <p className="text-black">Get started</p>
            </Button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;
