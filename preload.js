const { contextBridge, ipcRenderer } = require('electron')

contextBridge.exposeInMainWorld('api', {
  run: (payload) => ipcRenderer.invoke('run', payload),
  onLog: (cb) => ipcRenderer.on('log', (_e, line) => cb(line)),
})
