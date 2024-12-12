export const PublicRoutes = {
    LOGIN : '/login',  
    HOME : '/',
    ABOUT : '/about',
    CONTACT : '/contact',
    
};

export const EleccionRoute = {
    ELECCIONES: 'elecciones',
    DASHBOARD: 'dashboard',
    ELECCION: ':id',
    VOTAR: ':id/votar',
    RESULTADOS: ':id/resultados',
}

export const PrivateRoutes = {
    BASE: 'adm',
    DASHBOARD : 'dashboard',
    GESTIONAR_ELECCIONES : 'gestionar-elecciones',
    CREAR_ELECCION : 'crear-eleccion',
};

