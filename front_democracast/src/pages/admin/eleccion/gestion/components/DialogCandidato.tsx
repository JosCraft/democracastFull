import React, { useState } from "react";
import {
    Dialog,
    DialogContent,
    DialogDescription,
    DialogHeader,
    DialogTitle,
    DialogTrigger,
} from "@/components/ui/dialog";
import { IoIosPersonAdd } from "react-icons/io";
import { Button } from "@/components/ui/button";

export interface Persona {
    id?: number;
    nombre: string;
    apellido: string;
}

interface DialogCandidatoProps {
    personas: Persona[]; // Lista de personas existentes
    agregarCandidato: (persona: Persona) => void; // Función para agregar candidato
    registrarPersona: (persona: Persona) => void; // Función para registrar nueva persona
}

export const DialogCandidato = ({
    personas,
    agregarCandidato,
    registrarPersona,
}: DialogCandidatoProps) => {
    const [nuevaPersona, setNuevaPersona] = useState<Persona>({
        nombre: "",
        apellido: "",
    });

    const handleRegistroPersona = () => {
        if (nuevaPersona.nombre && nuevaPersona.apellido) {
            registrarPersona(nuevaPersona);
            setNuevaPersona({ nombre: "", apellido: "" }); // Reinicia el formulario
        } else {
            alert("Por favor, complete ambos campos.");
        }
    };

    return (
        <Dialog>
            <DialogTrigger className="flex justify-center items-center bg-red-800 hover:bg-red-500 p-2 rounded-md text-white">
                <IoIosPersonAdd className="mr-2" />
                Agregar Candidato
            </DialogTrigger>
            <DialogContent>
                <DialogHeader>
                    <DialogTitle>Agregar Candidato</DialogTitle>
                    <DialogDescription>
                        Selecciona una persona existente o registra una nueva.
                    </DialogDescription>
                </DialogHeader>

                {/* Tabla de personas existentes */}
                <div className="mt-4">
                    <h3 className="text-lg font-semibold">Personas registradas</h3>
                    <table className="table-auto w-full mt-2 border border-gray-200">
                        <thead>
                            <tr className="bg-gray-100">
                                <th className="px-4 py-2">Nombre</th>
                                <th className="px-4 py-2">Apellido</th>
                                <th className="px-4 py-2">Acción</th>
                            </tr>
                        </thead>
                        <tbody>
                            {personas.map((persona) => (
                                <tr key={persona.id} className="border-t">
                                    <td className="px-4 py-2">{persona.nombre}</td>
                                    <td className="px-4 py-2">{persona.apellido}</td>
                                    <td className="px-4 py-2">
                                        <Button
                                            onClick={() => agregarCandidato(persona)}
                                            className="bg-green-500 text-white px-3 py-1 rounded-md hover:bg-green-600"
                                        >
                                            Agregar
                                        </Button>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>

                {/* Formulario para registrar nueva persona */}
                <div className="mt-6">
                    <h3 className="text-lg font-semibold">Registrar nueva persona</h3>
                    <div className="mt-4">
                        <input
                            type="text"
                            placeholder="Nombre"
                            value={nuevaPersona.nombre}
                            onChange={(e) =>
                                setNuevaPersona((prev) => ({
                                    ...prev,
                                    nombre: e.target.value,
                                }))
                            }
                            className="border border-gray-300 rounded-md p-2 w-full mb-2"
                        />
                        <input
                            type="text"
                            placeholder="Apellido"
                            value={nuevaPersona.apellido}
                            onChange={(e) =>
                                setNuevaPersona((prev) => ({
                                    ...prev,
                                    apellido: e.target.value,
                                }))
                            }
                            className="border border-gray-300 rounded-md p-2 w-full"
                        />
                        <Button
                            onClick={handleRegistroPersona}
                            className="mt-4 bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600"
                        >
                            Registrar y Agregar
                        </Button>
                    </div>
                </div>
            </DialogContent>
        </Dialog>
    );
};
