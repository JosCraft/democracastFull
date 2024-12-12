import {
    Card,
    CardContent,
    CardTitle,
  } from "@/components/ui/card"
import { Button } from "@/components/ui/button"

const CardHome = () => {
    return (
        <Card
            className="w-[900px] h-[500px] p-6 shadow-lg flex items-center justify-center"
            style={{ marginTop: "15vh", position: "relative", background: "rgba(0,0,12,0.5)" }}
        >
            <CardContent className="text-center" style={{ position: "relative", zIndex: 2 }}>
                <CardTitle className="text-6xl font-bold text-amber-500 mb-8">
                    DEMOCRACAST
                </CardTitle>
                <Button className="w-[300px] py-4 text-lg font-semibold text-white bg-red-900 rounded-md hover:bg-amber-700" onClick={() => alert('asd')}>
                    Comenzar
                </Button>
            </CardContent>
        </Card>
    )
}
export default CardHome
