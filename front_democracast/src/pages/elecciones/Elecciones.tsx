import { lazy } from 'react';
import { RoutesNotFound } from '../../utilities';
import { EleccionRoute} from '../../models';
import { Navigate, Route, useParams } from 'react-router-dom';


const Dashboard = lazy(() => import('./dashboard/Dashboard'));
const Eleccion = lazy(() => import('./eleccion/Eleccion'));

const Elecciones = () => {

  const EleccionWrapper = () => {
    const { id } = useParams(); // Obtén el id dinámico de la URL
    return <Eleccion idEleccion={parseInt(id || '0')} />; // Pasa el id como prop
  };

  return (
    <RoutesNotFound>
        <Route path="/" element={<Navigate to={EleccionRoute.DASHBOARD} />} />
        <Route path={EleccionRoute.DASHBOARD} element={<Dashboard />} />
        <Route
        path={`${EleccionRoute.ELECCIONES}`}
        element={<EleccionWrapper />}
      />
    </RoutesNotFound>
  )
}

export default Elecciones
