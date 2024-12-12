import { lazy } from 'react';
import { RoutesNotFound } from '../../utilities';
import { PrivateRoutes } from '../../models';
import { Navigate, Route } from 'react-router-dom';

const Dashboard = lazy(() => import('./dashboard/Dashboard'));
const CrearEleccion = lazy(() => import('./eleccion/CrearEleccion'));
const Admin = () => {
  return (
    <RoutesNotFound>
        <Route path="/" element={<Navigate to={PrivateRoutes.DASHBOARD} />} />
        <Route path={PrivateRoutes.DASHBOARD} element={<Dashboard />} />
        <Route path={PrivateRoutes.CREAR_ELECCION} element={<CrearEleccion />} />

    </RoutesNotFound>
  )
}

export default Admin
