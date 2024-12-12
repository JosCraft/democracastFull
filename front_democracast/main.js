import { app, BrowserWindow } from 'electron';
import * as path from 'path';
import { fileURLToPath } from 'url';

// Obtener el directorio del archivo actual (en lugar de __dirname)
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

let win;

function createWindow() {
  win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'), // Asegúrate de tener un archivo preload.js
      nodeIntegration: true,
    },
  });

  win.loadURL('http://localhost:5173/'); // React en desarrollo

  // Hacer que la ventana ocupe toda la pantalla
  win.setFullScreen(true); // Esto pone la ventana en modo de pantalla completa

  win.on('closed', () => {
    win = null;
  });
}

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});
