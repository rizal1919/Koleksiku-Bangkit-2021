


var nama_pemain = prompt("Masukkan Namamu!");

var tanya = true;

alert("Selamat Datang di Permainan Suit Jawa " + nama_pemain);

user=0;
komp=0;
while (tanya){

	
	var p_user = prompt("Ayo bertaruh! Pilih Salah Satu\n Gajah | Semut | Orang");

	var pilihan_komp = Math.random();

	if (pilihan_komp <= 0.34){
		p_kom = "Gajah";
	}else if(pilihan_komp > 0.34 && pilihan_komp <= 0.67){
		p_kom = "Semut";
	}else{
		p_kom = "Orang";
	}
	

	
	if (p_user == "Gajah" || p_user == "gajah" || p_user == "GAJAH"){
		if(p_kom == "Gajah"){
			alert("HASIL SERI\nkomputer memilih " + p_kom + ", dan " + nama_pemain + " memilih " + p_user);
			
		}else if(p_kom == "Semut"){
			alert("KAMU KALAH\nkomputer memilih " + p_kom + ", dan " + nama_pemain + " memilih " + p_user);
			if (user === 0){
				user=user;
				komp+=1;
			}else if(user>0){
				user=user-1;
				komp+=1;
			}
		}else if(p_kom == "Orang"){
			alert("KAMU MENANG\nkomputer memilih " + p_kom + ", dan " + nama_pemain + " memilih " + p_user);
			if (komp === 0){
				komp=komp;
				user+=1;
			}else if(komp>0){
				komp=komp-1;
				user+=1;
			}
		}
	}
	
	else if(p_user == "Semut" || p_user == "semut" || p_user == "SEMUT"){
		if(p_kom == "Semut"){
			alert("HASIL SERI\nkomputer memilih " + p_kom + ", dan " + nama_pemain + " memilih " + p_user);
		}else if(p_kom == "Orang"){
			alert("KAMU KALAH\nkomputer memilih " + p_kom + ", dan " + nama_pemain + " memilih " + p_user);
			if (user === 0){
				user=user;
				komp+=1;
			}else if(user>0){
				user=user-1;
				komp+=1;
			}
		}else if(p_kom == "Gajah"){
			alert("KAMU MENANG\nkomputer memilih " + p_kom + ", dan " + nama_pemain + " memilih " + p_user);
			if (komp === 0){
				komp=komp;
				user+=1;
			}else if(komp>0){
				komp=komp-1;
				user+=1;
			}
		}
	
		
	}else if(p_user == "Orang" || p_user == "orang" || p_user == "ORANG"){
		if(p_kom == "Orang"){
			alert("HASIL SERI\nkomputer memilih " + p_kom + ", dan " + nama_pemain + " memilih " + p_user);
		}else if(p_kom == "Gajah"){
			alert("KAMU KALAH\nkomputer memilih " + p_kom + ", dan " + nama_pemain + " memilih " + p_user);
			if (user === 0){
				user=user;
				komp+=1;
			}else if(user>0){
				user=user-1;
				komp+=1;
			}
		}else if(p_kom == "Semut"){
			alert("KAMU MENANG\nkomputer memilih " + p_kom + ", dan " + nama_pemain + " memilih " + p_user);
			if (komp === 0){
				komp=komp;
				user+=1;
			}else if(komp>0){
				komp = komp - 1;
				user+=1;
			}
		}
		
		
	}else{
		alert("Masukkan pilihanmu dengan benar! Anjay");
	}
	
	
	alert("Skor Sementara :" + nama_pemain + ": " + user + " | Komputer : " + komp );
	var tanya = confirm("lagi?");
	if (tanya == false){

		if (user > komp){
			alert("===========< TERIMA KASIH >============\nHASIL AKHIR : [ " + nama_pemain + " = " + user + " | Komputer = " + komp + " ]\n===========< KAMU MENANG >============");
		}else{
			alert("===========< TERIMA KASIH >============\nHASIL AKHIR : [ " + nama_pemain + " = " + user + " | Komputer = " + komp + " ]\n===========< KAMU KALAH >==============");

		}
	}
	
}



/*
user=0;
komp=0;
var komp = parseInt(prompt());


if (komp === 0){
	komp=komp;
	user+=1;
}else if(komp>0){
	komp = komp - 1;
	user+=1;
}

alert(komp + " " + user)

*/