import React from "react";
import { View, Text, StyleSheet, TouchableOpacity } from "react-native";
import { useNavigation, useRoute } from "@react-navigation/native";

const MedicineDetail = () => {
  const navigation = useNavigation();
  const route = useRoute();
  const { medicine } = route.params;

  return (
    <View style={styles.container}>
      <Text style={styles.header}>{medicine.name} 상세 정보</Text>
      <Text style={styles.text}>처방일: {medicine.date}</Text>
      <Text style={styles.text}>남은 약: {medicine.remaining}</Text>
      <TouchableOpacity style={styles.backButton} onPress={() => navigation.goBack()}>
        <Text style={styles.backButtonText}>뒤로가기</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: "center", alignItems: "center", backgroundColor: "#fff" },
  header: { fontSize: 22, fontWeight: "bold", marginBottom: 20 },
  text: { fontSize: 16, marginBottom: 10 },
  backButton: {
    backgroundColor: "#FF8C8C",
    padding: 10,
    borderRadius: 10,
    marginTop: 20,
  },
  backButtonText: { color: "#fff", fontSize: 16, fontWeight: "bold" },
});

export default MedicineDetail;
