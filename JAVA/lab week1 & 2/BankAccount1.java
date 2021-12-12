//week 1 Q1.1
class Bank
{
	int amt;
	int bal;
	int acc_no;
	String name;
	
	void get_details()
	{
		System.out.println("CURRENT DETAILS");
		System.out.println("Account Number: "+acc_no);
		System.out.println("Name: "+name);
		System.out.println("Current Amount: "+bal);
	}
		
	void debit()
	{
		bal-=amt;
		System.out.println("Cash debitted");
		System.out.println("New balance: "+bal);
	}
	
	void credit()
	{
		bal+=amt;
		System.out.println("Cash credited");
		System.out.println("New balance: "+bal);
	}
}
class BankAccount1
{
	public static void main(String args[])
	{
		Bank object = new Bank();
		object.bal = 50000;
		object.name = "Tony";
		object.amt = 5000;
		object.acc_no = 123345;
		object.get_details();
		object.credit();
		object.debit();
	}
}
		
