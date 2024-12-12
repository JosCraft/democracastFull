import { MainContainer,  MainContent } from "./MainStyled";
import NavBar from "../nav/Navbar";

import { Toaster } from "@/components/ui/toaster";


interface MainProps {
  children: React.ReactNode;
}

const Main = ({ children }: MainProps) => {
  return (
    <MainContainer>
      <NavBar />
      <MainContent>{children}</MainContent>
      <Toaster />
    </MainContainer>
  );
};

export default Main;
