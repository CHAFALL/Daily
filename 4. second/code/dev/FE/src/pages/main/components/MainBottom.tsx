import { FaBusSimple } from 'react-icons/fa6';
import { useNavigate } from 'react-router-dom';

export const MainBottom = () => {
	const navigate = useNavigate();
	const userName = '김태용';

	const goSetDeparture = () => {
		navigate('/setDeparture');
	};

	const goSetArrival = () => {
		navigate('/setArrival');
	};
	return (
		<>
			<div className='fixed bottom-0 w-[100%] h-[35%] z-10 flex flex-col items-center bg-white border border-slate-200 rounded-t-[12px]'>
				<div className='w-[80%] font-["Pretendard-Bold"] text-[20px] mt-5'>{userName} 님 탑승</div>
				<div className='w-[80%] h-[36%] bg-white border-2 border-[#C4B5FC] rounded-lg divide-y divide-dashed divide-[#C4B5FC] my-7'>
					<div className='h-[50%] flex items-center' onClick={goSetDeparture}>
						<span className='mx-[5px]'>
							<FaBusSimple color='navy' className='mx-[5px]' />
						</span>
						<span className='mx-[5px]'>출발지 : {}</span>
					</div>
					<div className='h-[50%] flex items-center' onClick={goSetArrival}>
						<span className='mx-[5px]'>
							<FaBusSimple color='skyblue' className='mx-[5px]' />
						</span>
						<span className='mx-[5px]'>목적지 : {}</span>
						<span></span>
					</div>
				</div>
			</div>
		</>
	);
};