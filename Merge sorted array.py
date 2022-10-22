# a számok végétől kezdjük el csekkolni hogy melyik a nagyobb és csak simán a nums1 végétől kezdve berakosgatjuk

def merge(nums1, m, nums2, n):
    # amig vegig nem ertunk a csekkolason valamelyiknel
    while m > 0 and n > 0:
        # ha nums1 utolso szama nagyobb nums2 utolso szamanal
        if nums1[m - 1] > nums2[n - 1]:
            # nums1 utolso nullaja legyen nums1 utolso szama
            nums1[m + n - 1] = nums1[m - 1]
            # nums1ben egyel lentebbtol kezdjuk a csekkolast
            m -= 1
        else:
            # nums1 utolso nullaja legyen nums2 utolso szama
            nums1[m + n - 1] = nums2[n - 1]
            # nums2ben egyel lentebbtol kezdjuk a csekkolast
            n -= 1
    # hogyha nums2ben maradt szam de nums1ben mar nincs akkor ugye csak nagyobbak lehetnek tehat a vegere hozzakelladni
    while n > 0:
        nums1[n - 1] = nums2[n - 1]
        n -= 1
    return nums1


print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))
