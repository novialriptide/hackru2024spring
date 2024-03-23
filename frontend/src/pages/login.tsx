import Button from "../components/button";
import TextField from "../components/text-field";
import Tile from "../components/tile";

function Login() {
  return (
    <div>
      <div className="flex h-screen items-center justify-center bg-gradient-to-bl from-gray-600 via-gray-700 to-gray-800 text-center">
        <Tile>
          <div className="w-64 text-left">
            <div className="pt-4">
              <TextField required title="Username" htmlId="username" />
            </div>
            <div className="pt-4">
              <TextField
                required
                title="Password"
                htmlId="password"
                type="password"
              />
            </div>
            <div className="pt-4">
              <Button>
                <p className="text-gray-900">Login</p>
              </Button>
            </div>
          </div>
        </Tile>
      </div>
    </div>
  );
}

export default Login;
