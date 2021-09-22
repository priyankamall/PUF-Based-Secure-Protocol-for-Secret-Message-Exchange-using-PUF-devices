hashfunction h;
const XOR : Function;
const MatMul : Function ;
const Gen : Function ;
const Rep : Function;
protocol UserValidation(Ui, FD, CS)
{ 
	macro Bu = Gen(Bi);
	macro Au = h(IDu, PDu, h(Bu));
	macro Bu' = Rep(Bi', TCu');
	macro Au' = h(IDu, PDu, h(Bu'));
	macro Cu = XOR(Au, RNUu);
	macro Du = h(IDu, Au,RNUu);
	macro G1 = XOR(h(IDu,Au), Ru);
	macro RNUu' = XOR(Cu, Au');
	macro Du' = h(IDu, Au',RNUu');
	macro Ru' = XOR(G1,h(IDu,Au'));
	macro Ku = h(Tui,MatMul(Wx,Ru));
	macro Lu = h(IDu,IDCS,RNUu',Ru',Tui); 
	macro Mu = h(Wx,IDu,Ru,TFD);
	macro G2 = h(RNUu,Tui,TFD);
	macro K =h(IDu,IDCS,Ku,G2,TCS);
	macro Lu' = h(IDu,IDCS,RNUu,Ru,Tui);
	macro Mu' =h(Wx',IDu,Ru,TFD);
	macro G2' = h(RNUu',Tui,TFD);
	macro K' =h(IDu,IDCS,Ku,G2',TCS);
}	
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%		
role Ui
{ 
	var TFD, TCS : Nonce;
	fresh Tui: Nonce;
	const IDu, PDu, Bi, Bi', IDCS,
	TCu',RNUu,Ru,Wy,Wx,SKR :
	Ticket;
	send_1(Ui, FD, IDu, Au);
	recv_2(FD, Ui,Cu, Du, G1);
	match(Du, Du') ;
	send_3(Ui, FD, IDu, IDCS, Lu,Tui);
	recv_5(CS, Ui, K, G2, Wy, TCS,TFD);
	match(G2, G2');
	match(K, K');
	claim_Ui1(Ui,Secret,Tui);
	claim_Ui2(Ui,Secret,RNUu);
	claim_Ui3(Ui,Secret,Ru);
	claim_Ui4(Ui,Secret,Wy);
	claim_Ui6(Ui,SKR,Ku);
	claim_Ui7 (Ui,Niagree);
	claim_Ui8 (Ui,Nisynch);	
}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%			

role FD
{
	fresh TFD: Nonce;
	var Tui : Nonce;
	const IDu, PDu, IDCS, Bi,TCu',Tui, Bi',
	PDu, RNUu,Wx,Ru,Wy:
	Ticket;
	recv_1(Ui, FD, IDu, Au);
	send_2(FD, Ui,Cu, Du, G1);
	recv_3(Ui, FD, IDu, IDCS, Lu,Tui);
	match (Lu, Lu');
	send_4(FD, CS, Mu, G2, Ru, TFD,Tui);
	claim_FD1(FD,Secret,TFD);
	claim_FD2(FD,Secret,RNUu);
	claim_FD3(FD,Secret,Wx);
	claim_FD4(FD,Secret,Ru);
	claim_FD5(FD,Secret,Wy);
}
	       
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%			       

	       role CS
{
	var TFD, Tui: Nonce;
	fresh TCS : Nonce;
	const IDu, IDCS, Tui, Bi ,Bi',TCu',
	PDu,Wx,Wx',Ru,RNUu,Wy:
	Ticket;
	recv_4(FD, CS, Mu, G2, Ru, TFD,Tui);
	match(Mu, Mu');
	send_5(CS, Ui, K, G2, Wy, TCS,TFD);
	claim_CS1(CS,Secret,TFD);
	claim_CS2(CS, Secret, Wx');
	claim_CS3(CS, Secret, TCS);
	claim_CS4(CS,SKR,Ku);
}
}
