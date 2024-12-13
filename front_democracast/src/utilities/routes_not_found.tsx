import { Route, Routes} from 'react-router-dom';
import { NotFound } from '@/template';
interface Props{
    children: JSX.Element[] | JSX.Element	
}

const RoutesNotFound = ({children}:Props) => {
  return (
    <Routes>
      {children}
        <Route path="*" element={<NotFound/>}/>
    </Routes>
  )
}

export default RoutesNotFound;
