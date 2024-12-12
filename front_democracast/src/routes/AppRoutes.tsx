import { BrowserRouter, Route } from 'react-router-dom';
import { Suspense, lazy } from 'react';
import { RoutesNotFound } from '../utilities';
import { PublicRoutes } from '../models';
const Login = lazy(() => import('../pages/auth/login/Login'));
const HomePage = lazy(() => import('../pages/Home'));

const AppRoutes = () => {
  return (
    <Suspense fallback={<>Cargando</>}>
      <BrowserRouter>
        <RoutesNotFound>
          <Route path={PublicRoutes.HOME} element={<HomePage />} />
          <Route path={PublicRoutes.LOGIN} element={<Login/>}/>
          
        </RoutesNotFound>
      </BrowserRouter>
    </Suspense>
  );
};

export default AppRoutes;

