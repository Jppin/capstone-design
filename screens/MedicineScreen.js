import React, { useState } from "react";
import { View, Text, FlatList, TouchableOpacity, Switch, StyleSheet, TextInput } from "react-native";
import { useNavigation } from "@react-navigation/native";

const MedicineScreen = () => {
  const [medicines, setMedicines] = useState([
    { id: "1", name: "디곡신", date: "2024.10.22 처방", remaining: "10정 남음", active: true },
    { id: "2", name: "이지엔 6프...", date: "2024.10.22 처방", remaining: "10정 남음", active: false },
  ]);
  const navigation = useNavigation();

  const toggleMedicine = (id) => {
    setMedicines((prev) =>
      prev.map((medicine) =>
        medicine.id === id ? { ...medicine, active: !medicine.active } : medicine
      )
    );
  };

  return (
    <>
      <View style={styles.headerContainer}>
        <Text style={styles.header}>내 약품 보관함</Text>
        <TextInput style={styles.searchBar} placeholder="내 약 검색" />
      </View>
      <View style={styles.container}>
        <TouchableOpacity style={styles.addButton}>
          <Text style={styles.addButtonText}>+ 추가하기</Text>
        </TouchableOpacity>
        <FlatList
          data={medicines}
          keyExtractor={(item) => item.id}
          renderItem={({ item }) => (
            <View style={[styles.medicineCard, item.active ? styles.activeCard : styles.inactiveCard]}>
              <View style={styles.medicineInfo}>
                <Text style={styles.medicineName}>{item.name}</Text>
                <Text style={styles.medicineDate}>{item.date}</Text>
                <Text style={styles.medicineRemaining}>{item.remaining}</Text>
              </View>
              <Switch value={item.active} onValueChange={() => toggleMedicine(item.id)} />
              <TouchableOpacity onPress={() => navigation.navigate("./MedicineDetailScreen.js", { medicine: item })}>
                <Text style={styles.detailButton}>상세 정보 보기</Text>
              </TouchableOpacity>
            </View>
          )}
        />
      </View>
    </>

  );
};

const styles = StyleSheet.create({
  headerContainer: { 
    backgroundColor: "#FBAF8B", 
    padding: 20,
  },
  header: { 
    fontSize: 22, 
    fontWeight: "bold", 
    color: "#FFF", 
    alignItems: "flex-start"
   },
  searchBar: {
    width: "100%",
    backgroundColor: "#F5F5F5",
    borderRadius: 20,
    marginBlockStart:20,
    paddingHorizontal: 30,
    paddingVertical: 10,
    alignItems: "center", 
  },
  container: { flex: 1, backgroundColor: "#fff", padding: 20 },
  addButton: {
    backgroundColor: "#FF8E72",
    padding: 5,
    borderRadius: 5,
    alignItems: "center",
    marginBottom: 10,
    width: "25%",
  },
  addButtonText: { color: "#fff", fontSize: 14, fontWeight: "bold",},
  medicineCard: {
    flexDirection: "row",
    alignItems: "center",
    padding: 15,
    borderRadius: 10,
    marginBottom: 10,
  },
  activeCard: { backgroundColor: "#FFC1C1" },
  inactiveCard: { backgroundColor: "#EDEDED" },
  medicineInfo: { flex: 1 },
  medicineName: { fontSize: 16, fontWeight: "bold" },
  medicineDate: { fontSize: 12, color: "gray" },
  medicineRemaining: { fontSize: 12, color: "gray" },
  detailButton: { color: "#FF4081", fontSize: 14, fontWeight: "bold" },
});

export default MedicineScreen;
