import styled from "styled-components";
import logo from "@/assets/LOGO.png"; // Verifica que la ruta sea correcta

export const MainContainer = styled.div`

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

export const MainContent = styled.main` 
  flex-grow: 1; /* Equivalente a flex-grow */
`;