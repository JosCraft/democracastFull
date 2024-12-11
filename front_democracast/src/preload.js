const { contextBridge, ipcRenderer } = require('electron');

// Usando contextBridge para exponer funciones seguras al frontend de React
contextBridge.exposeInMainWorld('electron', {
  // Puedes exponer funciones que interactúan con Electron
  ping: () => ipcRenderer.send('ping'),
  onPong: (callback) => ipcRenderer.on('pong', callback)
});
