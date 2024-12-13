import {
    Card,
    CardFooter,
    CardContent,
    CardHeader,
    CardTitle,
} from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Candidato } from "@/components/interface";

interface CardCandidatosProps {
    candidato: Candidato;
    handleRemoveCandidato: (id: number) => void;
}

const CardCandidatos = ({ candidato, handleRemoveCandidato }: CardCandidatosProps) => {
    return (
        <Card
            className={`w-[180px] p-2 shadow-sm border rounded-md flex flex-col items-center
                bg-amber-50 text-slate-800`}
        >
            <CardHeader className="mb-1 w-full flex items-center justify-center">
                <div className="text-3xl font-bold text-red-700">
                    {candidato.numero_cartelera}
                </div>
            </CardHeader>
            <CardContent className="text-slate-700">
                <p className="text-xl truncate">
                    <span className="font-medium text-slate-800">
                        {candidato.nombre}
                    </span>
                </p>
            </CardContent>
            <CardFooter className="mt-2 w-full flex justify-center">
                <Button
                    variant="contained"
                    color="secondary"
                    onClick={() => handleRemoveCandidato(candidato.id)}
                    className="text-sm bg-red-500 text-white px-4 py-1 rounded-md hover:bg-red-600"
                >
                    Eliminar
                </Button>
            </CardFooter>
        </Card>
    );
};

export default CardCandidatos;
