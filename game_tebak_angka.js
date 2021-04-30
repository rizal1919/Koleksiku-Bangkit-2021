
alert("Kamu akan menebak sebuah angka dari 1-10");
var nama_pemain = prompt("Masukkan Nama Kamu");


function new_num() {
  // Statements 
  
	var angka_sementara = Math.random();

	if (angka_sementara >= 0.0 && angka_sementara < 0.1){
		angka_tebakan = 1;
	}else if(angka_sementara >= 0.1 && angka_sementara < 0.2){
		angka_tebakan = 2;
	}else if(angka_sementara >= 0.2 && angka_sementara < 0.3){
		angka_tebakan = 3;
	}else if(angka_sementara >= 0.3 && angka_sementara < 0.4){
		angka_tebakan = 4;
	}else if(angka_sementara >= 0.4 && angka_sementara < 0.5){
		angka_tebakan = 5;
	}else if(angka_sementara >= 0.5 && angka_sementara < 0.6){
		angka_tebakan = 6;
	}else if(angka_sementara >= 0.6 && angka_sementara < 0.7){
		angka_tebakan = 7;
	}else if(angka_sementara >= 0.7 && angka_sementara < 0.8){
		angka_tebakan = 8;
	}else if(angka_sementara >= 0.8 && angka_sementara < 0.9){
		angka_tebakan = 9;
	}else if(angka_sementara >= 0.9 && angka_sementara < 1.0){
		angka_tebakan = 10;
	}else{
		alert("tidak benar");
	}
	
	return angka_tebakan;
}

angka_tebakan = new_num();
var nanya = true;
var angka_inputan = 0;
var kesempatan = 0;
while(kesempatan <= 3 && nanya == true) {
	
	var angka_inputan = parseInt(prompt("Coba tebak! Tulis sebuah angka 1-10"));
	alert(angka_tebakan);
	if (angka_inputan === angka_tebakan){
		alert("Selamat " + nama_pemain + " \nKamu berhasil menebak angka " + angka_tebakan);
		var nanya = confirm("lagi?");
		if(nanya == true){
			kesempatan = 0;
			new_num();
		}else if(nanya==false){
			break;
		}
			
	}else if(angka_inputan < angka_tebakan){
		var jarak_angka = Math.abs(angka_tebakan-angka_inputan)
		alert("Kamu terlalu rendah " + jarak_angka + " angka");
	}else{
		var jarak_angka = Math.abs(angka_tebakan-angka_inputan)
		alert("Kamu terlalu tinggi " + jarak_angka + " angka");
	}
	kesempatan+=1;
	
	if (kesempatan == 3){
		var nanya = confirm("lagi?");
		if(nanya == true){
			kesempatan = kesempatan - 3;
		}else if(nanya == false){
			alert("Terima kasih "+ nama_pemain);
			break;
		}
	}
}


