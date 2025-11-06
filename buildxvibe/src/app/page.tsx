
import Navbar from '../components/navbar';
import GradientBlinds from '../components/GradientBlinds';
import { PlaceholdersAndVanishInputDemo } from '@/components/inputbox';
export default function Page() {
  return (
    <>
    <Navbar/>
        <div style={{ width: '100vw', height: '100vh', position: 'relative' }}>
            <GradientBlinds
                gradientColors={['#FF9FFC', '#5227FF']}
                angle={20}
                noise={0.3}
                blindCount={20}
                blindMinWidth={50}
                spotlightRadius={0.5}
                spotlightSoftness={1}
                spotlightOpacity={1}
                mouseDampening={0.15}
                distortAmount={0}
                shineDirection="left"
                mixBlendMode="lighten"
            />
            <div className="absolute top-0 left-0 w-full h-full flex items-center justify-center z-40 pointer-events-none ">
                <div className="pointer-events-auto">
                    <PlaceholdersAndVanishInputDemo />
                </div>
            </div>
        </div>
    </>
  )
}

