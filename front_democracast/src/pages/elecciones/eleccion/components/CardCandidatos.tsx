import {
    Card,
    CardFooter,
    CardContent,
    CardHeader,
    CardTitle,
  } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Candidato } from "@/components/interface"

interface CardCandidatosProps {
    candidato: Candidato;
    handleVotar: (candidato: Candidato) => void;
}
import { useState } from 'react'

const CardCandidatos = ({ candidato, handleVotar }: CardCandidatosProps) => {
    const [isVoted, setIsVoted] = useState(false); 

    const handleVotarClick = () => {
        setIsVoted(true); 
        handleVotar(candidato); 
    };

    return (
        <Card className="w-[300px] p-6 shadow-xl border rounded-lg bg-amber-100 flex flex-col items-start">
            <CardHeader className="mb-4 flex items-center justify-between w-full">
                <CardTitle className="text-xl font-semibold text-slate-800">
                    {candidato.numero_cartelera}
                </CardTitle>
            </CardHeader>
            <CardContent className="space-y-2 text-slate-700">
                <p className="text-sm">
                    Nombre: <span className="font-medium text-slate-800">{candidato.nombre}</span>
                </p>
            </CardContent>
            <CardFooter className="mt-4 w-full flex justify-end">
                <Button
                    className={`bg-amber-600 text-white hover:bg-red-700 px-4 py-2 rounded-md ${isVoted ? "bg-gray-400 cursor-not-allowed" : ""}`}
                    onClick={handleVotarClick}
                    disabled={isVoted} // Desactiva el botón después de votar
                >
                    {isVoted ? "Votado" : "Votar"}
                </Button>
            </CardFooter>
        </Card>
    );
};

export default CardCandidatos;

