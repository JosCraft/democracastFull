import { lazy } from 'react';
import { RoutesNotFound } from '../../utilities';
import { PrivateRoutes } from '../../models';
import { Navigate, Route } from 'react-router-dom';

const Dashboard = lazy(() => import('./dashboard/Dashboard'));

const Admin = () => {
  return (
    <RoutesNotFound>
        <Route path="/" element={<Navigate to={PrivateRoutes.DASHBOARD} />} />
        <Route path={PrivateRoutes.DASHBOARD} element={<Dashboard />} />
    </RoutesNotFound>
  )
}

export default Admin
