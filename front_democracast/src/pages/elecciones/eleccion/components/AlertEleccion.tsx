import {
    AlertDialog,
    AlertDialogAction,
    AlertDialogCancel,
    AlertDialogContent,
    AlertDialogDescription,
    AlertDialogFooter,
    AlertDialogHeader,
    AlertDialogTitle,
  } from "@/components/ui/alert-dialog";
  
  interface AlertEleccionProps {
    isOpen: boolean;
    onClose: () => void;
  }
  
  const AlertEleccion = ({ isOpen, onClose }: AlertEleccionProps) => {
    return (
<AlertDialog open={isOpen} onOpenChange={onClose}>
  <AlertDialogContent className="mb-1 w-full items-center justify-center bg-amber-100 border-4 border-red-950 rounded-md shadow-lg
    shadow-lg shadow-red-500/50
  ">
    <AlertDialogHeader className="mb-1 w-full items-center justify-center text-slate-800">
      <AlertDialogTitle className="text-3xl font-bold">GRACIAS POR PARTICIPAR</AlertDialogTitle>
    </AlertDialogHeader>
    <AlertDialogFooter className="mb-1 w-full flex items-center justify-center">
      <AlertDialogAction
        onClick={onClose}
        className="bg-amber-700 text-white font-semibold py-2 px-4 rounded hover:bg-amber-800 focus:ring-2 focus:ring-amber-600"
      >
        Aceptar
      </AlertDialogAction>
    </AlertDialogFooter>
  </AlertDialogContent>
</AlertDialog>

    );
  };
  
  export default AlertEleccion;
  