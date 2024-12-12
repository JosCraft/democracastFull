import { MainContainer,  MainContent } from "./MainStyled";
import NavBar from "../nav/Navbar";

interface MainProps {
  children: React.ReactNode;
}

const Main = ({ children }: MainProps) => {
  return (
    <MainContainer>
      <NavBar />
      <MainContent>{children}</MainContent>
    </MainContainer>
  );
};

export default Main;
