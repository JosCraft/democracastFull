import { useNavigate } from "react-router-dom"; // Importa useNavigate
import { EleccionRoute } from '@/models'; // Ajusta la ruta según corresponda
import { Button } from "../ui/button";
const ParticiparButton = ({ id }: { id: string }) => {
    const navigate = useNavigate(); // Usamos el hook useNavigate

    const handleParticipar = () => {
        navigate(`/${EleccionRoute.ELECCIONES}/${EleccionRoute.ELECCION.replace(':id', id)}`); // Redirige a la ruta de la elección con el id
    };

    return (
        <Button 
            className="bg-amber-600 text-white hover:bg-amber-900 px-4 py-2 rounded-md"
            onClick={handleParticipar} // Llama a handleParticipar al hacer clic
        >
            Participar
        </Button>
    );
};

export default ParticiparButton;
