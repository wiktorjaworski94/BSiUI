import md5



#function h($s) {
#  $s = md5('Sx12s;!,.alxMausA_!s'.$s);
#  $s = substr($s, 0, 16); // 64 bity
#
#  return $s;
#}


def h(s):
	m=md5.new()
	m.update(s)
	m = str(m)
	return m


costam = "test"
print(costam)
costam = h(costam)
print(costam)
