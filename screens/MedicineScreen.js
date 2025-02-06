import React, { useState } from "react";
import { 
  View, Text, FlatList, TouchableOpacity, Switch, 
  StyleSheet, TextInput, Modal, Pressable
} from "react-native";
import MaterialIcons from "react-native-vector-icons/MaterialIcons";

const MedicineHeader = ({ search, setSearch }) => (
  <View style={styles.headerContainer}>
    <Text style={styles.headerText}>내 약품 보관함</Text>
    <View style={styles.searchContainer}>
      <TextInput 
        style={styles.searchBox}
        placeholder="내 약 검색"
        value={search}
        onChangeText={setSearch}
      />
      <MaterialIcons name="search" size={24} color="#999" style={styles.searchIcon} />
    </View>
  </View>
);

const MedicineScreen = ({ navigation }) => {
  const [medicines, setMedicines] = useState([
    { id: "1", name: "디곡신", date: "2024.10.22 처방", remaining: "10정 남음", active: true },
    { id: "2", name: "이지엔 6프...", date: "2024.10.22 처방", remaining: "10정 남음", active: false },
  ]);
  const [search, setSearch] = useState("");
  const [isModalVisible, setIsModalVisible] = useState(false);
  const [isSortMenuVisible, setIsSortMenuVisible] = useState(false);

  const toggleMedicine = (id) => {
    setMedicines((prev) =>
      prev.map((medicine) =>
        medicine.id === id ? { ...medicine, active: !medicine.active } : medicine
      )
    );
  };

  return (
    <>
      <MedicineHeader search={search} setSearch={setSearch} />
      <View style={styles.container}>
        {/* 필터 & 정렬 + 추가하기 버튼 */}
        <View style={styles.actionContainer}>
          <TouchableOpacity style={styles.addButton} onPress={() => setIsModalVisible(true)}>
            <Text style={styles.addButtonText}>+ 추가하기</Text>
          </TouchableOpacity>
          <View style={styles.filterSortContainer}>
            <TouchableOpacity style={styles.filterButton}>
              <MaterialIcons name="filter-list" size={18} color="#333" />
              <Text style={styles.filterText}> 필터</Text>
            </TouchableOpacity>
            <TouchableOpacity style={styles.sortButton} onPress={() => setIsSortMenuVisible(!isSortMenuVisible)}>
              <MaterialIcons name="sort" size={18} color="#333" />
              <Text style={styles.filterText}> 정렬</Text>
            </TouchableOpacity>
          </View>
        </View>

        {/* 정렬 팝업 */}
        {isSortMenuVisible && (
          <View style={styles.sortPopup}>
            <TouchableOpacity onPress={() => setIsSortMenuVisible(false)}>
              <Text style={styles.sortOption}>가나다순</Text>
            </TouchableOpacity>
            <TouchableOpacity onPress={() => setIsSortMenuVisible(false)}>
              <Text style={styles.sortOption}>날짜순</Text>
            </TouchableOpacity>
          </View>
        )}

        {/* 약품 리스트 */}
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
              <Switch 
                value={item.active} 
                onValueChange={() => toggleMedicine(item.id)}
                trackColor={{ false: "#ddd", true: "#FFA07A" }}
                thumbColor={item.active ? "#FFA07A" : "#f4f3f4"}
              />
              <TouchableOpacity onPress={() => navigation.navigate("MedicineDetail", { medicine: item })}>
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
  container: { flex: 1, backgroundColor: "#f8f8f8", paddingHorizontal: 15 },

  /* 헤더 (검색창 포함) */
  headerContainer: { 
    backgroundColor: "#FFA07A", 
    paddingVertical: 20, 
    paddingHorizontal: 20,
    borderBottomLeftRadius: 20, 
    borderBottomRightRadius: 20 
  },
  headerText: { fontSize: 22, fontWeight: "bold", color: "white", textAlign: "left", marginBottom: 10 },

  /* 검색창 */
  searchContainer: { flexDirection: "row", alignItems: "center", backgroundColor: "white", borderRadius: 20, paddingHorizontal: 15 },
  searchBox: { flex: 1, paddingVertical: 8, fontSize: 14 },
  searchIcon: { marginLeft: 5 },

  /* 필터 & 정렬 버튼 */
  actionContainer: { flexDirection: "row", justifyContent: "space-between", marginVertical: 10 },
  addButton: { backgroundColor: "#FFA07A", padding: 10, borderRadius: 10 },
  addButtonText: { color: "white", fontWeight: "bold" },

  /* 정렬 팝업 */
  sortPopup: {
    position: "absolute",
    top: 45,
    right: 0,
    backgroundColor: "rgba(0, 0, 0, 0.8)",
    borderRadius: 8,
    paddingVertical: 8,
    paddingHorizontal: 12,
    zIndex: 100,
  },
  sortOption: {
    color: "#fff",
    fontSize: 14,
    paddingVertical: 6,
  },

  /* 약품 리스트 스타일 */
  medicineCard: { flexDirection: "row", alignItems: "center", padding: 15, borderRadius: 10, backgroundColor: "white", marginBottom: 10 },
  activeCard: { borderLeftWidth: 5, borderColor: "#FFA07A" },
  inactiveCard: { borderLeftWidth: 5, borderColor: "#ddd" },
});

export default MedicineScreen;
