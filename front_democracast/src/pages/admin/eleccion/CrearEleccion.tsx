import React, { useState } from "react";
import { Label, Input, Button } from "@/components/ui";
import { FaExclamationCircle } from "react-icons/fa";
import { Main } from "@/template";
import { toast } from "@/hooks/use-toast";

const CrearEleccion = () => {
  const [formData, setFormData] = useState({
    nombre_eleccion: "",
    descripcion_eleccion: "",
    fecha_eleccion: new Date().toISOString().split("T")[0], 
    votos_permitidos_eleccion: "1", 
  });

  const [errors, setErrors] = useState({
    nombre_eleccion: "",
    descripcion_eleccion: "",
    fecha_eleccion: "",
    votos_permitidos_eleccion: "",
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
    setErrors({ ...errors, [name]: "" });
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const newErrors = validateForm();
    if (Object.values(newErrors).some((error) => error)) {
      setErrors(newErrors);
      return;
    }
    console.log("Formulario enviado", formData);
    toast({
        title: "Eleccion creada",
        description: "La elección ha sido creada exitosamente.",
        type: "success",
    });
  };

  const validateForm = () => {
    const newErrors: typeof errors = {
      nombre_eleccion: "",
      descripcion_eleccion: "",
      fecha_eleccion: "",
      votos_permitidos_eleccion: "",
    };

    if (!formData.nombre_eleccion.trim())
      newErrors.nombre_eleccion = "El nombre es obligatorio.";
    if (!formData.descripcion_eleccion.trim())
      newErrors.descripcion_eleccion = "La descripción es obligatoria.";
    if (!formData.fecha_eleccion)
      newErrors.fecha_eleccion = "La fecha es obligatoria.";
    if (!formData.votos_permitidos_eleccion || +formData.votos_permitidos_eleccion <= 0)
      newErrors.votos_permitidos_eleccion =
        "Debe ingresar un número mayor a 0 para los votos permitidos.";

    return newErrors;
  };

  return (
    <Main>
        <div className="max-w-md mx-auto p-6 rounded-lg shadow-md"
            style={{ marginTop: "15vh", position: "relative", background: "rgba(149, 149, 149, 0.3)" }}
        >
      <h1 className="text-4xl font-bold text-amber-400 mb-6">Crear Elección</h1>
      <form onSubmit={handleSubmit} className="space-y-4">
        <div className="text-amber-100">
          <Label htmlFor="nombre_eleccion" className="text-amber-100">
            Nombre
          </Label>
          <Input
            type="text"
            id="nombre_eleccion"
            name="nombre_eleccion"
            value={formData.nombre_eleccion}
            onChange={handleChange}
            className="mt-1 text-amber-100"
          />
          {errors.nombre_eleccion && (
            <p className="flex items-center text-red-600 text-sm mt-1">
              <FaExclamationCircle className="mr-1" />
              {errors.nombre_eleccion}
            </p>
          )}
        </div>

        <div>
          <Label htmlFor="descripcion_eleccion" className="text-amber-100">
            Descripción
          </Label>
          <Input
            type="text"
            id="descripcion_eleccion"
            name="descripcion_eleccion"
            value={formData.descripcion_eleccion}
            onChange={handleChange}
            className="mt-1 text-amber-100"
          />
          {errors.descripcion_eleccion && (
            <p className="flex items-center text-red-600 text-sm mt-1">
              <FaExclamationCircle className="mr-1" />
              {errors.descripcion_eleccion}
            </p>
          )}
        </div>

        <div>
          <Label htmlFor="fecha_eleccion" className="text-amber-100">
            Fecha
          </Label>
          <Input
            type="date"
            id="fecha_eleccion"
            name="fecha_eleccion"
            value={formData.fecha_eleccion}
            onChange={handleChange}
            className="mt-1 text-amber-100"
          />
          {errors.fecha_eleccion && (
            <p className="flex items-center text-red-600 text-sm mt-1">
              <FaExclamationCircle className="mr-1" />
              {errors.fecha_eleccion}
            </p>
          )}
        </div>

        <div>
          <Label htmlFor="votos_permitidos_eleccion" className="text-amber-100">
            Votos Permitidos por Persona
          </Label>
          <Input
            type="number"
            id="votos_permitidos_eleccion"
            name="votos_permitidos_eleccion"
            value={formData.votos_permitidos_eleccion}
            placeholder={1}
            onChange={handleChange}
            className="mt-1 text-amber-100"
          />
          {errors.votos_permitidos_eleccion && (
            <p className="flex items-center text-red-600 text-sm mt-1">
              <FaExclamationCircle className="mr-1" />
              {errors.votos_permitidos_eleccion}
            </p>
          )}
        </div>

        <Button
          type="submit"
          className="w-full bg-amber-700 text-white font-semibold py-2 rounded hover:bg-amber-800 transition"
        >
          Crear Elección
        </Button>
      </form>
    </div>
    </Main>
  );
};

export default CrearEleccion;
