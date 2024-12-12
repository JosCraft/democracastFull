import logo from '@/assets/LOGO.png';
import { ReactNode } from "react";
import NavBar from "../nav/Navbar";

interface MainProps {
    children: ReactNode;
}

const Main = ({ children }: MainProps) => {
  return (
    <div className="bg-stone-900 flex flex-col h-screen w-screen items-center justify-center relative"> 
        <NavBar />
        <main className="flex-grow"> 
            {children}
        </main>
        <div className="absolute inset-0 opacity-10 bg-no-repeat bg-center bg-contain" style={{ backgroundImage: `url(${logo})` }}></div>
    </div>
  );
}

export default Main;
