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
        <Card
            className={`w-[180px] p-2 shadow-sm border rounded-md flex flex-col items-center
                transition ease-in-out delay-150 hover:-translate-y-1 hover:scale-110 hover:bg-amber-500 duration-300
                ${
                    isVoted
                        ? "bg-gray-300 text-gray-500 cursor-not-allowed transition-none" 
                        : "bg-amber-50 text-slate-800 cursor-pointer"
                }`}
            onClick={!isVoted ? handleVotarClick : undefined}
        >
            <CardHeader className="mb-1 w-full flex items-center justify-center">
                <div className={`text-3xl font-bold ${isVoted ? "text-gray-500" : "text-red-700"}`}>
                    {candidato.numero_cartelera}
                </div>
            </CardHeader>
            <CardContent className={`text-slate-700 ${isVoted ? "text-gray-500" : ""}`}>
                <p className="text-xl truncate">
                    <span className={`font-medium ${isVoted ? "text-gray-500" : "text-slate-800"}`}>
                        {candidato.nombre}
                    </span>
                </p>
            </CardContent>
            <CardFooter className="mt-2 w-full flex justify-center"></CardFooter>
        </Card>
    );
    
};

export default CardCandidatos;

