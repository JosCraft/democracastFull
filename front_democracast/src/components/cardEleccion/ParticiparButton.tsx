import { useNavigate } from "react-router-dom"; 
import { EleccionRoute } from '@/models'; 
import { Button } from "../ui/button";

interface ParticiparButtonProps {
    id: string;
    cantidadVotos: number;
}

const ParticiparButton = ({ id, cantidadVotos }: ParticiparButtonProps ) => {
    const navigate = useNavigate();

    const handleParticipar = () => {
        localStorage.setItem('cantidadVotos', cantidadVotos.toString());
        console.log(localStorage.getItem('cantidadVotos'));
        navigate(`/${EleccionRoute.ELECCIONES}/${EleccionRoute.ELECCION.replace(':id', id)}`);
    };

    return (
        <Button 
            className="bg-amber-600 text-white hover:bg-amber-900 px-4 py-2 rounded-md"
            onClick={handleParticipar}
        >
            Participar
        </Button>
    );
};

export default ParticiparButton;
