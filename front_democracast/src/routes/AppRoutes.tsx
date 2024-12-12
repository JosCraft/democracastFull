import { BrowserRouter, Route } from 'react-router-dom';
import { Suspense, lazy } from 'react';
import { RoutesNotFound } from '../utilities';
import { EleccionRoute, PrivateRoutes, PublicRoutes } from '../models';

const Login = lazy(() => import('../pages/auth/login/Login'));
const HomePage = lazy(() => import('../pages/home/Home'));
const Admin = lazy(() => import('../pages/admin/Admin'));
const Elecciones = lazy(() => import('../pages/elecciones/Elecciones'));

const AppRoutes = () => {
  return (
    <Suspense fallback={<>Cargando</>}>
      <BrowserRouter>
        <RoutesNotFound>
          <Route path={PublicRoutes.HOME} element={<HomePage />} />
          <Route path={PublicRoutes.LOGIN} element={<Login/>}/>
          {/*Rutas ADMIN*/ }
          <Route path={`${PrivateRoutes.BASE}/*`} element={<Admin/>} />
          {/* Rutas Electores */}
          <Route path={`${EleccionRoute.ELECCIONES}/*`} element={<Elecciones/>} />
        </RoutesNotFound>
      </BrowserRouter>
    </Suspense>
  );
};

export default AppRoutes;

