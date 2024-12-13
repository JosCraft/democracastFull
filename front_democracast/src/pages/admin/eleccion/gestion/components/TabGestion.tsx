import * as React from 'react';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import Box from '@mui/material/Box';
import Datos from './Datos';
import Candidatos from './Candidatos';

interface TabPanelProps {
  children?: React.ReactNode;
  index: number;
  value: number;
}

function CustomTabPanel(props: TabPanelProps) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`simple-tabpanel-${index}`}
      aria-labelledby={`simple-tab-${index}`}
      {...other}
    >
      {value === index && <Box sx={{ p: 3 }}>{children}</Box>}
    </div>
  );
}

function a11yProps(index: number) {
  return {
    id: `simple-tab-${index}`,
    'aria-controls': `simple-tabpanel-${index}`,
  };
}

export default function TabsGestion() {
  const [value, setValue] = React.useState(0);

  const handleChange = (event: React.SyntheticEvent, newValue: number) => {
    setValue(newValue);
  };

  return (
    <Box sx={{ width: '100%' }}>
      <Box
        sx={{
          borderBottom: 1,
          borderColor: 'divider',
          '& .MuiTabs-indicator': {
            backgroundColor: '#f59e0b', // Amber indicator
          },
        }}
      >
        <Tabs
          value={value}
          onChange={handleChange}
          aria-label="tabs gestion"
          TabIndicatorProps={{
            style: { backgroundColor: '#f59e0b' },
          }}
          variant="scrollable"
          scrollButtons="auto"
        >
          <Tab
            label="Datos Elección"
            {...a11yProps(0)}
            sx={{
              '&.Mui-selected': { color: '#f59e0b' },
              textTransform: 'none',
              fontWeight: 'bold',
              color: '#a8a29e',
            }}
          />
          <Tab
            label="Candidatos"
            {...a11yProps(1)}
            sx={{
              '&.Mui-selected': { color: '#f59e0b' },
              textTransform: 'none',
              fontWeight: 'bold',
              color: '#a8a29e',
            }}
          />
          <Tab
            label="Resultados"
            {...a11yProps(2)}
            sx={{
              '&.Mui-selected': { color: '#f59e0b' },
              textTransform: 'none',
              fontWeight: 'bold',
              color: '#a8a29e',
            }}
          />
          <Tab
            label="Máquinas"
            {...a11yProps(3)}
            sx={{
              '&.Mui-selected': { color: '#f59e0b' },
              textTransform: 'none',
              fontWeight: 'bold',
              color: '#a8a29e',
            }}
          />
          <Tab
            label="Nueva Ronda"
            {...a11yProps(4)}
            sx={{
              '&.Mui-selected': { color: '#f59e0b' },
              textTransform: 'none',
              fontWeight: 'bold',
              color: '#a8a29e',
            }}
          />
          <Tab
            label="Finalizar"
            {...a11yProps(5)}
            sx={{
              '&.Mui-selected': { color: '#f59e0b' },
              textTransform: 'none',
              fontWeight: 'bold',
              color: '#a8a29e',
            }}
          />
        </Tabs>
      </Box>
      <CustomTabPanel value={value} index={0}>
        <Datos/>
      </CustomTabPanel>
      <CustomTabPanel value={value} index={1}>
        <Candidatos/>
      </CustomTabPanel>
      <CustomTabPanel value={value} index={2}>
        <h2 className="text-amber-500 font-semibold">Resultados</h2>
        <p>Aquí puedes ver los resultados de la elección.</p>
      </CustomTabPanel>
      <CustomTabPanel value={value} index={3}>
        <h2 className="text-amber-500 font-semibold">Máquinas</h2>
        <p>Aquí puedes gestionar las máquinas de votación.</p>
      </CustomTabPanel>
      <CustomTabPanel value={value} index={4}>
        <h2 className="text-amber-500 font-semibold">Nueva Ronda</h2>
        <p>Aquí puedes iniciar una nueva ronda de votaciones.</p>
      </CustomTabPanel>
      <CustomTabPanel value={value} index={5}>
        <h2 className="text-amber-500 font-semibold">Finalizar</h2>
        <p>Aquí puedes finalizar la elección.</p>
      </CustomTabPanel>
    </Box>
  );
}
