import React from 'react'
import { useNavigate } from "react-router-dom"; 
import styled from "styled-components";
import logo from "@/assets/LOGO.png";
import { Button } from "@/components";

const NotFound = () => {
    const navigate = useNavigate();
    const handleGoHome = () => {
        navigate('/');
    }
    const MainContainer = styled.div`
    background: 
        linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), /* Añade un efecto para opacidad */
        url(${logo}) no-repeat center/contain; /* Fondo con imagen */
    background-color: #1c1c1c; /* Fondo principal en caso de que no cargue la imagen */

    display: flex;
    flex-direction: column;
    height: 100vh; /* Altura completa de la pantalla */
    width: 100vw; /* Ancho completo de la pantalla */
    align-items: center;
    justify-content: center;
    position: relative;
    `;

    const ErrorTitle = styled.h1`
  color: white;
  font-size: 30rem;
  margin: 0;
`;

const ErrorSubtitle = styled.h2`
  color: white;
  font-size: 8rem;
  margin: 0;
  margin-bottom: 20px;
`;

    const StyledButton = styled(Button)`
  background-color: #ff4757;
  color: white;
  padding: 40px;
  font-size: 2.2rem;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;

  &:hover {
    background-color: #ff6b81;
  }
`;

  return (
    <MainContainer>
      <StyledButton onClick={handleGoHome}>Regresar</StyledButton>
    </MainContainer>
  )
}

export default NotFound
