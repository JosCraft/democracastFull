import { useState, useEffect } from "react";
import NavBarStyle from "./NavBarStyle";
import { Button } from "@/components/ui/button";
import { Menu, X } from "lucide-react";
import { FaHome, FaInfoCircle, FaStore } from 'react-icons/fa';
import { CiPaperplane } from "react-icons/ci";
import { IoAddCircleOutline } from "react-icons/io5";
import { CiEdit } from "react-icons/ci";

const Navbar = () => {
    const [isOpen, setIsOpen] = useState(false);
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [role, setRole] = useState<string | null>(null);
    const [name, setName ] = useState<string | null>(null);



    const toggleMenu = () => {
        setIsOpen(!isOpen);
    };

    const handleLogin = () => {
        window.location.href = "/login"; 
    };

    const handleRegister = () => {
        window.location.href = "/register"
    }


    const handleLogout = () => {
        localStorage.removeItem('authToken'); 
        setIsAuthenticated(false);
        window.location.reload(); 
    };

    return (
        <header className="bg-red-950 text-plate-50 shadow-md  w-screen">
            <NavBarStyle>
                <nav className="container mx-auto px-4 py-3 flex justify-between items-center">
                    <ul className="hidden md:flex space-x-6">
                        <li>
                            <a href="/" className="link text-amber-300 hover:text-amber-500 transition-colors duration-200">
                                <FaHome size={20} />
                                Inicio
                            </a>
                        </li>
                        <li>
                            <a href="/shop" className="link text-amber-300 hover:text-amber-500 transition-colors duration-200">
                                <CiPaperplane size={20} />
                                Elecciones
                            </a>
                        </li>
                        <li>
                            <a href="/shop" className="link text-amber-300 hover:text-amber-500 transition-colors duration-200">
                                <IoAddCircleOutline size={20} />
                                Crear Eleccion
                            </a>
                        </li>
                        <li>
                            <a href="/shop" className="link text-amber-300 hover:text-amber-500 transition-colors duration-200">
                                <CiEdit size={20} />
                                Gestionar Elecciones
                            </a>
                        </li>
                    </ul>

                    <Button
                        className="bg-orange-400 md:hidden text-white focus:outline-none focus:ring-2 focus:ring-white rounded hover:bg-orange-600"
                        onClick={toggleMenu}
                        aria-label="Toggle Menu"
                    >
                        {isOpen ? <X size={24} /> : <Menu size={24} />}
                    </Button>
                </nav>

                {isOpen && (
                    <div className="bg-orange-900 text-amber-50 hover:text-amber-400 md:hidden">
                        <ul className="flex flex-col space-y-2 px-4 py-2">
                            <li>
                                <a href="/" className="block py-2 px-4 link text-white hover:bg-orange-400 rounded transition-colors duration-200">
                                    <FaHome size={20} /> Inicio
                                </a>
                            </li>
                            <li>
                                <a href="/shop" className="block py-2 px-4 link hover:text-amber-400 transition-colors duration-200">
                                    <FaStore size={20} />
                                    Tienda
                                </a>
                            </li>
                        </ul>
                    </div>
                )}
            </NavBarStyle>
        </header>
    );
};

export default Navbar;
