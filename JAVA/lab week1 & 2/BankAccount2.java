//week 1 Q1.2

class Bank
{
	int amt;
	int bal;
	int acc_no;
	
	void set_details(int a, int b)
	{
		acc_no = a;
		bal = b;
	}
	void get_details()
	{
		System.out.println("CURRENT DETAILS");
		System.out.println("Account Number: "+acc_no);
		System.out.println("Current Amount: "+bal);
	}
	
	void debit(int amt)
	{
		bal-=amt;
		System.out.println("Cash debitted");
		System.out.println("New balance: "+bal);
	}
	
	void credit(int amt)
	{
		bal+=amt;
		System.out.println("Cash credited");
		System.out.println("New balance: "+bal);
	}
}
class BankAccount2
{
	public static void main(String args[])
	{
		Bank object = new Bank();
		object.set_details(12233444,50000);
		object.get_details();
		object.debit(5000);
		object.credit(5000);
		
			Bank object2 = new Bank();
		object2.set_details(8484733, 10000);
		object2.get_details();
		object2.debit(5000);
		object2.credit(5000);
	}
	}
	





